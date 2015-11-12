# rpigcc

These scripts generate an RPM package for the RaspBerryPi Linux X64 cross-compiler.

The original compiler is available at https://github.com/raspberrypi/tools.

Clone this repository on an RPM-enabled system and run `make'. You should end-up with 
an installable RPM package that:

  * Puts all neccessary tools and libraries into /usr/lib/rpigcc.
  * Links all binaries (arm-linux-gnueabihf-*) in /usr/bin to have them in the path.
  
