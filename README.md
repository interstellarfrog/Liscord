# Liscord
Chat App Made In Python For Same Network Communication or Port Forwarding

Running On Windows

![ftCdSkbjBb](https://user-images.githubusercontent.com/119659110/231225541-d76a7c7b-2a49-46e0-8e8f-7750172fb486.png)


Running On Arch Linux - You Have To Install Tkinter - sudo pacman -S tk

![Screenshot 2023-05-01 123702](https://user-images.githubusercontent.com/119659110/235446709-a6fb013e-ca90-4cd6-a4a6-4b1a40415e41.png)




# Disclaimer

# This Code Is Really Really Bad Nearly Unreadable

I am not planning to fix this or work on this project at all

# I AM NOT RESPONSIBLE IF ANYTHING BAD HAPPENS


This was Made as a first year college project for computing science Do not expect it to work
Without errors and I would not use this for anything important as im not sure how secure the
application is exactly, and do not expect the code to be written in a good way or documented 
at all as I did write this some time ago. The only external connection appart from the ones 
that you connect to is https://api.ipify.org/ to get the public IP for connecting cross network
I am unsure if cross network works though as I have not tested this.

# Description 

This application uses PyQt5 to make a GUI app that can be used for same network communication 
and might work for cross network communication using port forwarding. 
I am unsure if this works on anything but windows, but feel free to test it the app uses port 55555.
There is a help menu built into the app if you dont know what you are doing and since there is no server the apps 
basically control each other by sending commands between each other say something like
starting a call the app would then send a request to the other app and then the other
user can choose to accept it or not. The screenshare also starts automatically on the other persons 
screen when started so i'd be careful about this. The chat part of the app is encrypted using the 
RSA library which I decided to add to the project at 4am on the last day so also do not expect this
to be secure or work at all but I checked it on wireshark before finishing so it should be fine.

# Known Errors

The only errors I know of are within the modules I was using at the time which are made by nueral nine 
which is the screenshare and voice share modules called vidstream if I had more time I would have made
these myself but sometimes when pressing the call or screenshare buttons allot it will start 2 calls or screenshares
now that I think about it I should have added a short time limit before allowing start of another call or 
screenshare.
