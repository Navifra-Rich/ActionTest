FROM navifra/ros:noetic-desktop-focal3

RUN git clone https://github.com/eclipse/paho.mqtt.cpp.git && \
    cd paho.mqtt.cpp  && git checkout v1.4.0 && \
    git submodule init &&  git submodule update && \
    cmake -Bbuild -H. -DPAHO_WITH_SSL=OFF -DPAHO_ENABLE_TESTING=OFF -DPAHO_BUILD_DEB_PACKAGE=OFF -DPAHO_WITH_MQTT_C=ON && \
    sudo cmake --build build/ --target install

RUN rm -rf paho.mqtt.cpp

WORKDIR /home/navifra