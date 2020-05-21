## Код команды <TEAMNAME>

Протестированно с версиями ПО python=3, ros=melodic, os=Ubuntu 18.04, Arch linux, Debian Buster
## Установка зависимостей
```bash
pip3 install numpy
pip3 install opencv-python
pip3 install pyzbar
```
## Запуск
### В виде ROS пакета
 - Создать catkin workspace 
 - Поместить файлы пакета в папку src workspace`а
 - Cкомпелировать пакет ior2020_<TEAMNAME>_copter_vision  (выполнить ``` catkin_make``` в папке workspace`a )
 - выполнить ``` source devel/setup.bash``` в папке workspace`a 
#### Для Color Recognition
```bash
roslaunch ior2020_<TEAMNAME>_copter_vision <TEAMNAME>_colorDetecting_withCam.launch
```
#### Для Qr Recognition
```bash
roslaunch ior2020_<TEAMNAME>_copter_vision <TEAMNAME>_qrCode_withCam.launch
```
### В виде отдельных python файлов
перед запуском файлов проекта в ручную необходимо запустить ноду работы с камерой 
```python3 src/<TEAMNAME>_cam.py```
#### Для Color Recognition
```bash
python3 src/<TEAMNAME>_colorDetecting.py
```
#### Для Qr Recognition
```bash
python3 src/<TEAMNAME>_qrCode.py
```