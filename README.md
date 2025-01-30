<p align=center>
  <br>
  <img src="Mypros_Weather.png"/>
  <br>
  <span><b>A simple tool to get the weather of any place in the world.</b></span>
  <br>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/JimmyTarson12/Mypros-Weather/blob/main/LICENSE">License</a>
</p>

<a name="installation"></a>
## Installation
### Docker
Pull the latest version of the repository from Docker hub
```bash
docker pull mypro12/mypros-weather:latest
```

<a name="usage"></a>
## Usage
To run it with the default location of New York City:
```bash
docker run mypro12/mypros-weather:latest
```
You can specify certain coordinates:
```bash
docker run -e LATITUDE=51.5074 -e LONGITUDE=-0.1278 mypro12/mypros-weather:latest
```
<br>
<br>
<div align=center>
  
  [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/mypro12)
  
</div>
