前言：
目前很多搭载100系列芯片组的机型（如HP gaming精灵系列机型）在改装WIN7时会遇到USB接口失灵的问题，这是因为100系列芯片组采用XHCI主控接口，移除了之前芯片组中的EHCI主控接口，而WIN7系统原生并不支持XHCI主控接口，所以不论用U盘还是USB光驱等设备安装系统时会安装失败，用部署命令的方式集成USB3.0驱动又太繁琐，这让我等WIN7粉丝很头疼，好在Intel也注意到了我们的需求，适时的提供了一个小工具可以方便的将USB3.0驱动集成进ISO镜像中，简单易用，下面给大家介绍一下具体方法
一、首先下载Win7 USB3.0 Creator程序

https://downloadmirror.intel.com/25476/eng/Win7_USB3.0_Creator_v2.zip
二、将Win7 USB3.0 Creator v2解压缩
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/2f16de160924ab182f3f43dd33fae6cd7a890b9b.jpg)
USB_3.0_Win7_64_4.0.0.36文件夹内是要整合进ISO的驱动文件
Installer_Creator.exe是安装程序
Installer_Creator_readme.pdf是英文说明文件，英文好的童靴也可以参考这个说明
三、插上用WindowsUSB/DVD Download Tool制作的WIN7系统U盘（其他如UltraISO制作的U盘介质理论上也可以），右键点击Installer_Creator.exe，选择以管理员身份运行（若不以管理员身份运行会有如下图中的Program must be run in Administrator的提示，导致无法继续）
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/ad660724ab18972b6d13a220e0cd7b899f510a9b.jpg)

四、点击右侧的...浏览路径，选择WIN7系统U盘，确定
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/7454a518972bd4078fee71177d899e510eb3099b.jpg)

五、点击Create Image按钮
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/d668992bd40735fa5dd9ec5398510fb30e24089b.jpg)

六、开始修改U盘中的系统镜像文件，原版WIN7（测试版本windows7 ultimate sp1 x64） ISO镜像会检测到4个WIM镜像需要修改，持续最长15分钟左右即可结束
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/ea5bda0735fae6cdc79d098b09b30f2443a70f9b.jpg)
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/a9773bfae6cd7b8923459869092442a7d8330e9b.jpg)

七、看到Update finished!制作结束，将做好的WIN7系统U盘插到要安装系统的机器上（经测试任意USB接口皆可）正常从U盘引导（如果开机提示No bootable device建议更换U盘重新制作）
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/488ae8cd7b899e51b1a798fe44a7d933c9950d9b.jpg)

八、安装系统过程中未出现需要加载USB3.0控制器驱动的提示，安装过程中外接的USB鼠标，键盘皆可用；通过此工具修改的WIN7安装U盘在安装完系统后，设备管理器里直接带有USB3.0控制器驱动无需再单独安装，所有USB2.0和3.0接口皆可直接连接设备使用
![img](Intel%E7%AC%AC%E5%85%AD%E4%BB%A3%E5%A4%84%E7%90%86%E5%99%A8Skylake%E5%B9%B3%E5%8F%B0%E5%AE%89%E8%A3%85Windows%207.assets/9bbd75899e510fb3b030d57ddf33c895d0430c9b.jpg)