# Код команды L22_**ÆRO**

Протестированно с версиями ПО python=3, ros=melodic, os=Ubuntu 18.04, Arch linux, Debian Buster, Windows 10
## Установка зависимостей
```bash
pip3 install numpy
pip3 install opencv-python
pip3 install pyzbar
```
## Запуск
### В виде ROS пакета
 <!-- - Создать catkin workspace 
 - Поместить файлы пакета в папку src workspace`а
 - Cкомпелировать пакет ior2020_L22_AERO_copter_vision  (выполнить ``` catkin_make``` в папке workspace`a )
 - выполнить ``` source devel/setup.bash``` в папке workspace`a  -->
 - выполнить catkin_make в папке ior_ws
 - выполнить source devel/setup.bash
#### Для Color Recognition
```bash
roslaunch ior2020_L22_AERO_copter_vision L22_AERO_colorDetecting_withCam.launch
```
#### Для Qr Recognition
```bash
roslaunch ior2020_L22_AERO_copter_vision L22_AERO_qrCode_withCam.launch
```
### В виде отдельных python файлов
перед запуском файлов проекта в ручную необходимо запустить ноду работы с камерой и roscore
```bash
roscore &
python3 ior_ws/src/ior2020_l22_aero_copter_vision/src/L22_AERO_cam.py
```
#### Для Color Recognition
```bash
python3 ior_ws/src/ior2020_l22_aero_copter_vision/src/L22_AERO_colorDetecting.py
```
#### Для Qr Recognition
```bash
python3 ior_ws/src/ior2020_l22_aero_copter_vision/src/L22_AERO_qrCode.py
```
-----------

```


      ___                 ___                 ___                 ___     
     /\  \               /\  \               /\  \               /\  \    
    /::\  \             /::\  \             /::\  \             /::\  \   
   /:/\:\  \           /:/\:\  \           /:/\:\  \           /:/\:\  \  
  /::\~\:\  \         /::\~\:\  \         /::\~\:\  \         /:/  \:\  \ 
 /:/\:\ \:\__\       /:/\:\ \:\__\       /:/\:\ \:\__\       /:/__/ \:\__\
 \/__\:\/:/  /       \:\~\:\ \/__/       \/_|::\/:/  /       \:\  \ /:/  /
      \::/  /         \:\ \:\__\            |:|::/  /         \:\  /:/  / 
      /:/  /           \:\ \/__/            |:|\/__/           \:\/:/  /  
     /:/  /             \:\__\              |:|  |              \::/  /   
     \/__/               \/__/               \|__|               \/__/    


```

-----------
L22_**ÆRO**
