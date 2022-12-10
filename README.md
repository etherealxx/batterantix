<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/etherealxx/audiotracksmerger">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Batterantix</h3>

<p align="center">
    Simple 'Battery Low' notification for AntiX Linux.
    <br />
    <!-- <a href="https://github.com/etherealxx/audiotracksmerger"><strong>Explore the docs »</strong></a> -->
    <!-- <br /> -->
    <!-- <br /> -->
<!--     <a href="https://github.com/etherealxx/audiotracksmerger">View Demo</a>  -->
<!--    · -->
<!--     <a href="https://github.com/etherealxx/audiotracksmerger/releases/download/v0.1.4/Audio.Tracks.Merger.ffmpeg.exe">Clone Repo</a> -->
<!--     · -->
<!--     <a href="https://github.com/etherealxx/audiotracksmerger/releases/download/v0.1.4/Audio.Tracks.Merger.ffmpeg.x86.exe">Download Zip</a> -->
<!--     · -->
<!--     <a href="https://github.com/etherealxx/audiotracksmerger/releases/download/v0.1.4/Audio.Tracks.Merger.bat">Download tar.gz</a> -->
<!--     · -->
    <a href="https://github.com/etherealxx/audiotracksmerger/issues">Report Bug</a>
    ·
    <a href="https://github.com/etherealxx/audiotracksmerger/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#language-used">Language Used</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#settingscustomization">Settings/Customization</a></li>
    <li><a href="#additional-note">Additional Note</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

AntiX is a great distro. It's lightweight and easy to use. It comes with different flavor, and the Full flavor are jam-packed with many useful tools to do almost everything. However there is one important feature that is forgotten: the low battery notification<br />

It's annoying that sometimes your laptop turn off immediately without warning in the middle of work. This simple script i provided will fix that annoyance. It uses python script and `Zenity` to send notification popup that warns user when the battery hits certain threshold. Also there is an optional script that turn off your computer if the battery hit the 'critical' threshold.

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

### Language used

* Python
* Bash

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- GETTING STARTED -->


## Prerequisites

If you're on a new device, `apt update` is mandatory, atleast once. `apt upgrade` is recommended but not required. <br />

```bash
sudo apt update
```

Then install these two important packages that will be used: `git` and `zenity`. `git` will be used to clone the repo (download the scipt) to your local storage. And `zenity` will be used to show a popup notification<br />

```bash
sudo apt-get install git
sudo apt-get install zenity
```

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- USAGE EXAMPLES -->

## Installation

1. Clone the repository to your local storage

```bash
git clone https://github.com/etherealxx/batterantix
```

2. Change directory into the script directory

```bash
cd batterantix
```

3. Allow `execute` permission on every script there

```bash
chmod +x $PWD/*
```

4. Edit the `~/.bashrc` file, so that the script can be ran everywhere. You can use any text editor you like, here i'll use `geany`

```bash
geany ~/.bashrc
```

    Add this line to the end of the text file, then save the text file

```bash
export PATH=$PATH:/home/$USER/batterantix
```

    (assuming you didn't move the script's folder, and the git clone happened in     `/home/<yourusername>/`)

5. Now edit the `startup` file so that the scipt will run everytime the laptop boots. (Note that you can use other text editor other than `geany`)

```bash
geany /home/ethereal/.desktop-session/startup
```

    Add this line to the end of the text file, then save the text file

```bash
batterantix.py &
```

    At this point the main script are ready to go, but the next step to 'automatically turn off the laptop when critical battery' are recommended.

6. Edit the `rc.local` file so that the critical battery script will run as superuser everytime the laptop boots. (The shutdown command won't run without superuser. Note that you can use other text editor other than `geany`

```bash
sudo geany /etc/rc.local
```

    Add this line to the text file **before** the `exit 0` line, then save the text file

```
batterantixcrit.py &
```

Finally, restart your laptop. If there's a popup few seconds after boot, the code works and installed successfully.

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

## Settings/Customization

You can edit the line 6 and 7 of `batterantix` to customize the low battery and critical battery threshold of your likings.

```bash
lowBatteryPercentage = 10
criticalBatteryPercentage = 4
```

Don't forget to also edit the line 6 of `batterantixcrit` if you want to.

## Additional Note

If you, for some reason, still want to continue your project even if the battery is low, and don't want to be annoyed by the notification constantly popping up, type this to your terminal

```bash
sudo killbatt.py
```

It will kill all Batterantix process, and you need to restart your laptop to make the script run normally again.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- LICENSE -->

## License

Distributed under the GNU GPLv3 License. See `LICENSE.md` for more information.

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTACT -->

## Contact

etherealxx - gwathon3@gmail.com

Project Link: [https://github.com/etherealxx/batterantix](https://github.com/etherealxx/batterantix)

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

* [README.md Template](https://github.com/othneildrew/Best-README-Template)

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->
