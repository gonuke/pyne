from fortranformat import FortranRecordReader
import math
class Mctal(object):
     def __init__(self):
        pass

     def read(self, filename):
        """Parses a 'mctal' tally output file from MCNP. Currently this
        only supports reading the kcode data- the remaining tally data
        will not be read.
        """

        # open file
        self.f = open(filename, 'r')

        # get code name, version, date/time, etc
        # using fortran format

        words = self.f.readline()
        # specify fortran format for code name, version,date/time, etc
        ff=FortranRecordReader('(2A8,A19,I5,I11,I15)')
        words=ff.read(words)

        self.code_name = words[0]
        self.code_version = words[1]
        self.code_date_time = words[2]

        #self.code_time = words[3]
        self.n_dump = words[3]
        #self.n_histories = int(words[4])
        #self.n_prn = int(words[5])

        # comment line of input file
        # self.comment = self.f.readline().strip()
        ff=FortranRecordReader('(1x,A79)')
        words=self.f.readline()
        self.comment= ff.read(words)
        self.comment = [item for item in self.comment if item is not None]
        
        # read tally line
        words = self.f.readline()
        # specify fortran format for tally line
        ff=FortranRecordReader('(A4,I6,1x,A5,I6)')
        words=ff.read(words)
        self.n_tallies = words[1]
        try:
          self.n_perts = words[4]
        except IndexError:
        # if perturbations not existing in mctal files,set it to default value 0
          self.n_perts = 0
        #if len(words) > 2:
            # perturbation tallies ?present
        #   pass

        # read tally numbers

        if self.n_tallies!=0:
          num_lines_tally_num = math.ceil(self.n_tallies/16)
          ff = FortranRecordReader('(16I5)')
          words = self.f.readline()
          tally_nums=ff.read(words)
          
          for i in range(1,num_lines_tally_num):
             words = self.f.readline()
             tally_nums = ff.read(words) + tally_nums
          tally_nums = [item for item in tally_nums if item is not None]
        # read tallies
        for i_tal in tally_nums:
            pass
        
        # routinely read tally information
        for num in range(self.n_tallies):
            words = self.f.readline()
            ff = FortranRecordReader('(A5,3I5)')
            tally = ff.read(words)
            problem_name = tally[1]
            particle_type = tally[2]
            tally_type = tally[3]
        

            words = self.f.readline()
            if words.startswith(" "):
            # read FC card lines
              ff = FortranRecordReader('(5x,A75)')
              self.FC_card_lines = ff.read(words)
              words = self.f.readline()
              while words.startswith(" "):
                 self.FC_card_lines = ff.read(words) + self.FC_card_lines
                 words = self.f.readline()

            # read f lines
            ff = FortranRecordReader('(A2,I8)')
            f = ff.read(words)
            num_cell = f[1]
            if num_cell != 0 and tally_type != 1:
               cell_num_lines = math.ceil(num_cell/11) 
               words = self.f.readline()
               ff = FortranRecordReader('(11I7)')
               cell_nums = ff.read(words)
           
               for i in range(1,cell_num_lines):
                  words = self.f.readline()
                  cell_nums = cell_nums + words
           
               cell_nums = [item for item in cell_nums if item is not None]
            words = self.f.readline()
            # read d line
            ff = FortranRecordReader('(A2,I8)')
            n = ff.read(words)
            total_flagged_unflagged =n[1]

            # read user bins line
            words = self.f.readline()
            user_bins=ff.read(words)
            user_bins_nums = user_bins[1]

            # read segment bins line
            words = self.f.readline()
            segment_bin = ff.read(words)
            segment_bins_nums = segment_bin[1]

            # read multipiler bin line
            words = self.f.readline()
            multiplier_bin = ff.read(words)
            multiplier_bins_nums = multiplier_bin[1]
            # read cosine values
            words = self.f.readline()
            ff = FortranRecordReader('(A2,I8,I4)')
            cos = ff.read(words)
            cosine_bin_num = cos[1]
            if cosine_bin_num != 0:
               cos_val_lines = cosine_bin_num//6+1
               ff = FortranRecordReader('(1P6E13.5)')
               words = self.f.readline()
               cos_val = ff.read(words)
               for i in range(1,cos_val_lines):
                   words = self.f.readline()
                   cos_val = cos_val + ff.read(words)
               cos_val = [item for item in cos_val if item is not None]

            # read energy bin line
            words = self.f.readline()
            ff = FortranRecordReader('(A2,I8,I4)')
            energy_bin = ff.read(words)
            energy_bin_num = energy_bin[1]
            if energy_bin_num !=0:
               energy_val_lines = math.ceil(energy_bin_num/6)
               ff = FortranRecordReader('(1P6E13.5)')
               words = self.f.readline()
               energy_val = ff.read(words)
               for i in range(1,energy_val_lines):
                   words = self.f.readline()
                   energy_val = energy_val + ff.read(words)

               energy_val = [item for item in energy_val if item is not None]
            # read time bin line
            words = self.f.readline()
            ff = FortranRecordReader('(A2,I8,I4)')
            time_bin = ff.read(words)
            time_bin_num = time_bin[1]
            if time_bin_num != 0:
                time_val_lines = math.ceil(time_bin_num/6)
                ff = FortranRecordReader('(1P6E13.5)')
                words = self.f.readline()
                time_val = ff.read(words)
                for i in range(1,time_val_lines):
                    words = self.f.readline()
                    time_val = time_val + ff.read(words)
                time_val = [item for item in time_val if item is not None]
            # read VALS
            self.f.readline()
            words = self.f.readline()
            ff = FortranRecordReader('(4(1PE13.5,0PF7.4))')
            vals = ff.read(words)
            words = self.f.readline()
            while words.startswith(" "):
                vals = ff.read(words) + vals
                words = self.f.readline()
        
            vals = [val for val in vals if val is not None]
            # read TFC lines
            ff = FortranRecordReader('(A3,I5,8I8)')
            tfc = ff.read(words)
            tally_fluc_set_num = tfc[1]
            words = self.f.readline()
            ff = FortranRecordReader('(I11,1P3E13.5)')
            tally_fluc = ff.read(words)
            if tally_fluc_set_num != 0:
                for i in range(1,tally_fluc_set_num):
                    words = self.f.readline()
                    tally_fluc = tally_fluc + ff.read(words)

                tally_fluc = [item for item in tally_fluc if item is not None]

