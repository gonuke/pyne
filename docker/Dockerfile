ARG uversion=20.04
FROM ubuntu:${uversion} as base

# Ubuntu Setup
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV HOME /root
RUN apt-get update \
    && apt-get install -y --fix-missing \
            software-properties-common \
            wget \
            g++ \
            build-essential \
            python3-setuptools \
            python3-pip \
            python3-setuptools \
            python3-dev \
            libpython3-dev \
            git \
            cmake \
            gfortran \
            vim emacs \
            libblas-dev \
            liblapack-dev \
            libeigen3-dev \
            libhdf5-dev \
            libhdf5-serial-dev \
            autoconf \
            libtool \
            doxygen \
            hdf5-tools \
    && apt-get clean -y \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10 \
    && pip install --force-reinstall \
            sphinx \
            cloud_sptheme \
            prettytable \
            sphinxcontrib_bibtex \
            numpydoc \
            nbconvert \
            numpy \
            nose \
            cython \
            future \
            matplotlib \
            tables \
            scipy \
            jinja2 \
            progress

# make starting directory
RUN mkdir -p $HOME/opt

FROM base as moab

ARG build_moab="YES"
ARG enable_pymoab="YES"
ARG build_dagmc="YES"
ENV INSTALL_PATH=$HOME/opt/moab

# build MOAB
RUN if [ "$build_moab" = "YES" ] || [ "$enable_pymoab" = "YES" ] || [ "$build_dagmc" = "YES" ]; then \
        if [ "$enable_pymoab" = "YES" ] ; \
        then \ 
            export PYMOAB_FLAG="-DENABLE_PYMOAB=ON"; \
        fi \
        && echo $PYMOAB_FLAG \
        && mkdir -p $INSTALL_PATH \
        && cd $INSTALL_PATH \
        && git clone --depth 1 --single-branch -b 5.4.0 https://bitbucket.org/fathomteam/moab \
        && cd moab \
        && mkdir bld \
        && cd bld \
      # build/install shared lib
        && cmake .. \
              ${PYMOAB_FLAG} \
              -DCMAKE_INSTALL_PREFIX=$INSTALL_PATH \
              -DENABLE_HDF5=ON \
              -DBUILD_SHARED_LIBS=ON \
              -DENABLE_BLASLAPACK=OFF \
              -DENABLE_FORTRAN=OFF \
        && make -j 3 \
        && make install \
        && cd ../.. \
        && rm -rf moab ; \
    fi

# put MOAB on the path
ENV LD_LIBRARY_PATH $HOME/opt/moab/lib:$LD_LIBRARY_PATH
ENV LIBRARY_PATH $HOME/opt/moab/lib:$LIBRARY_PATH
ENV PYTHONPATH=$HOME/opt/moab/lib/python3.8/site-packages/

FROM moab as dagmc

ARG build_dagmc="YES"

# build/install DAGMC
ENV INSTALL_PATH=$HOME/opt/dagmc
RUN if [ "$build_dagmc" = "YES" ]; then \
        mkdir -p $INSTALL_PATH \
        && cd $INSTALL_PATH \
        && git clone --depth 1 --branch stable https://github.com/svalinn/DAGMC.git \
        && cd DAGMC \
        && mkdir bld \
        && cd bld \
        && cmake .. -DMOAB_DIR=$HOME/opt/moab \
                 -DCMAKE_INSTALL_PREFIX=$INSTALL_PATH \
                 -DBUILD_STATIC_LIBS=OFF \
                 -DBUILD_UWUW=OFF \
                 -DBUILD_TALLY=OFF \
                 -DBUILD_MAKE_WATERTIGHT=OFF \
                 -DBUILD_OVERLAP_CHECK=OFF \
                 -DBUILD_TESTS=OFF \
        && make -j 3\
        && make install \
        && cd ../.. \
        && rm -rf DAGMC; \
    fi

FROM dagmc as openmc

# build/install OpenMC Python API
ARG install_openmc="YES"
ENV INSTALL_PATH=$HOME/opt/openmc
RUN if [ "$install_openmc" = "YES" ]; then \
        mkdir -p ${INSTALL_PATH} \
        && cd ${INSTALL_PATH} \
        && git clone https://github.com/openmc-dev/openmc.git \
        && cd openmc \
        && git checkout v0.12.2 \
        && pip install . ; \
    fi

FROM openmc AS pyne 

ARG build_pyne=YES
# Build/Install PyNE
RUN if [ "$build_pyne" = "YES" ]; then \
        cd $HOME/opt \
        && git clone -b develop --single-branch https://github.com/pyne/pyne.git \
        && cd pyne \
        && python setup.py install --user \
                                    --moab $HOME/opt/moab --dagmc $HOME/opt/dagmc \
                                    --clean -j 3; \
    fi
ENV PATH $HOME/.local/bin:$PATH
RUN if [ "$build_pyne" = "YES" ]; then \
        cd $HOME \
        && nuc_data_make ; \
    fi



