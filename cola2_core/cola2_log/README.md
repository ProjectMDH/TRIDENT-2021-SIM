# COLA2_LOG package

This package contains nodes related to the logging/storing cola2 parameters and data.

The `default_param_handler` node requires the python module `ruamel.yaml`. To install it:

```bash
pip install ruamel.yaml
```

To check whether the PC boots and shutdowns correctly, the shutdown logger startup process can be installed using systemd to start at boot:

```bash
# copy to systemd folder
sudo cp startup_processes/shutdown_logger_startup_process.service /etc/systemd/system/
# reload to have the new service
sudo systemctl --system daemon-reload
# add as start process
sudo systemctl enable shutdown_logger_startup_process
# reboot
sudo reboot
```

[TOC]

[//]: <> (bag_recorder start)

## bag_recorder

**Node**: /bag_recorder

This node provides services to start and stop the launch_bag.launch, which is in charge of recording bag files with a custom configuration.

![bag_recorder](doc/readme/bag_recorder.svg)

**Publishers**: None


**Subscribers**: None


**Services**:

* /bag_recorder/disable_logs [[std_srvs/Trigger](http://docs.ros.org/melodic/api/std_srvs/html/srv/Trigger.html)]
* /bag_recorder/enable_logs [[std_srvs/Trigger](http://docs.ros.org/melodic/api/std_srvs/html/srv/Trigger.html)]

**Parameters**: None


[//]: <> (bag_recorder end)

[//]: <> (computer_logger start)

## computer_logger

**Node**: /computer_logger

This node publishes CPU/RAM usage data and temperature of the vehicle's computer.

![computer_logger](doc/readme/computer_logger.svg)

**Publishers**:

* /computer_logger/cpu_usage [[std_msgs/Float32](http://docs.ros.org/melodic/api/std_msgs/html/msg/Float32.html)]
* /computer_logger/ram_usage [[std_msgs/Float32](http://docs.ros.org/melodic/api/std_msgs/html/msg/Float32.html)]
* /computer_logger/temperature [[sensor_msgs/Temperature](http://docs.ros.org/melodic/api/sensor_msgs/html/msg/Temperature.html)]
* /diagnostics [[diagnostic_msgs/DiagnosticArray](http://docs.ros.org/melodic/api/diagnostic_msgs/html/msg/DiagnosticArray.html)]

**Subscribers**: None


**Services**: None


**Parameters**: None


[//]: <> (computer_logger end)

[//]: <> (default_param_handler start)

## default_param_handler

**Node**: /default_param_handler

This node provides services to store current parameters in the rosparam server as defaults by writing them to their corresponding .YAML files.

![default_param_handler](doc/readme/default_param_handler.svg)

**Publishers**: None


**Subscribers**: None


**Services**:

* /default_param_handler/update_param_in_yaml [[cola2_msgs/String](http://api.iquarobotics.com/202010/api/cola2_msgs/html/srv/String.html)]
* /default_param_handler/update_params_in_yamls [[std_srvs/Trigger](http://docs.ros.org/melodic/api/std_srvs/html/srv/Trigger.html)]

**Parameters**:

* /default_param_handler/config_folder
* /default_param_handler/config_pkg

[//]: <> (default_param_handler end)

[//]: <> (param_logger start)

## param_logger

**Node**: /param_logger

This node publishes all parameters loaded in the rosparam server in a string topic for logging/debugging purposes.

![param_logger](doc/readme/param_logger.svg)

**Publishers**:

* /diagnostics [[diagnostic_msgs/DiagnosticArray](http://docs.ros.org/melodic/api/diagnostic_msgs/html/msg/DiagnosticArray.html)]
* /param_logger/params_string [[std_msgs/String](http://docs.ros.org/melodic/api/std_msgs/html/msg/String.html)]

**Subscribers**: None


**Services**:

* /param_logger/publish_params [[std_srvs/Trigger](http://docs.ros.org/melodic/api/std_srvs/html/srv/Trigger.html)]

**Parameters**: None


[//]: <> (param_logger end)