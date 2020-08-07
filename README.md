## Demo Video
https://youtu.be/c4PtBs9bxEM

## Summary
The average American walks approximately 3,500 steps per day; each step creates mechanical energy, energy which ends up being wasted and dispersed into the environment. Tapping into this wasted energy opens a door for opportunities to supplement the user’s actions. Varying amounts of piezoelectric sensors were used to generate this energy which gets stored in a LiPo battery through the aid of the BQ25570 chip. My design used 33 piezoelectric sensors, which generated, approximately 0.27 volts or 23.625 mAh just after 60 steps. If a user wore this shoe and walked the average amount of steps per day, they would generate 1,378.125 mAh! In addition, I developed an add-on to this project that adds an Arduino Nano with an Accelerometer and Gyroscope sensor. The data from these sensors are run through a neural network that predicts the behavior the user is doing. For example, if the user is jumping it will predict they are jumping.

## How I built it
The hardware component of this project has one layer of styrofoam on the top and bottom. This protects the piezoelectric sensors and increases comfort for the user. Then there are two layers of cardboard, each side of the cardboard has 8-9 piezoelectric sensors, connected in series. The two cardboard pieces are connected in parallel. There is then a thin piece of paper between the two cardboard pieces, to make sure no wires short out when they touch each other.  

The software uses Keras with TensorFlow. I created a Google Cloud Virtual Machine Instance, which runs a python script that reads in data regarding user's motion and then with Keras and TensorFlow creates a model of the data that can be used for prediction. 

## Challenges I ran into
Developing the hardware of the shoes took the bulk of my time. I have never used Piezoelectric sensors before, so I had to learn how to use them. In addition, it took me a while to optimize the energy outputted from the shoe. The green BQ25570 chip helped me do that though.

## Accomplishments that I'm proud of
This is the world's most efficient shoe that generates electricity! Other solutions mostly use different means to generate electricity. My solution used Piezoelectric sensors, and then the BQ25570 chip to control the flow of electricity from the two capacitors on the chip to the battery. This minimizes the electricity wasted. 

## What I learned
I learned a lot! In general, I am better at software related projects, this project, being a hardware-first project, increased my skills in dealing with hardware. I got better at soldering, understanding the mathematical calculations of voltage and current, Piezoelectric sensors, Arduinos and various hardware compounds. On the software side, this was my first time using Google Cloud. I am now comfortable in creating complex Virtual Machines in the cloud that can run various advanced scripts. 

## What's next for Generating Electricity By Walking
I want to add a wifi/Bluetooth chip into the Arduino Nano, this will enable the data from the accelerometer and gyroscope to transfer to a web server in the cloud without the need of a wire. With this advancement, I could develop a mobile/web app that tracks various foot-related fitness activities, including jumping, running and walking. 
