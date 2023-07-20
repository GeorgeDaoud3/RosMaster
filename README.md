# RosMaster
# Introduction

![Untitled](figures/1.png)

Astra Camera has 

1. IR camera: for a gray IR image
2. RGB camera: for an RGB camera
3. IR projector and distance sensors: for a depth image
4. microphone

To capture the three kinds of images, we start by launching the vehicle with the Astra camera

```bash
roslaunch yahboomcar_nav astrapro_bringup.launch
```

To capture and display depth images, we should run 

```bash
rosrun astra_show  depth_viewer.py
```

To capture and display IR images, we should run 

```bash
rosrun astra_show  ir_viewer.py
```

To capture and display rgb images, we should run 

```bash
rosrun astra_show  rgb_viewer.py
```

![Untitled](figures/2.png)

## Rqt Graph

![Untitled](figures/3.png)

The **/camera** namespace contains all the nodes and topics for Astra Camera. The **/camera/camera_nodelet_manager** will start and stop the stream. The streaming is done trough the topics

- **/camera/ir/image**
- **/camera/depth_registered/image**
- **/camera/rgb/image_rect_color**
