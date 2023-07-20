# RosMaster
# Introduction

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9d610bc6-abb4-4ae7-9d70-6e4f5e6685dd/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0da1b0fc-f857-46be-8f25-f57407ae41bf/Untitled.png)

## Rqt Graph

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c0b1711-79c7-44f2-b411-1197f4223b8a/Untitled.png)

The **/camera** namespace contains all the nodes and topics for Astra Camera. The **/camera/camera_nodelet_manager** will start and stop the stream. The streaming is done trough the topics

- **/camera/ir/image**
- **/camera/depth_registered/image**
- **/camera/rgb/image_rect_color**
