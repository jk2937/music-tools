MIT License

Copyright (c) 2023 Jonathan David Kaschak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

About:

This repository, called music-tools, contains miscellaneous Python scripts
related to music. My goal with this repository is to develop the code into 
a suite of music software which will include a step-sequencer, a synthesizer
which will include several modules including an ai module capable of 
generating instrument sounds based off of keywords, a tool for quickly performing
music theory calculations, and a tool for creating complex midi patterns at
the click of a button using musical serialism techniques.

ChatGPT:

In addition to developing music software, I will be experimenting with ChatGPT
and documenting the results. 

chatgpt-tonegen:

The folder chatgpt-tonegen currently contains 
synthesizer code written by ChatGPT, as well as audio renders created by this
code. Soon, I will update it to contain my chat logs with ChatGPT, for the 
sake of reproducibility. 

Please be aware that the audio files in the chatgpt-tonegen folder are very 
loud, as they are intended to be used as resources during music production. 
Turn your speakers down before listening to them!

chatgpt-gui:

This folder contains synthesizer with GUI code written by ChatGPT. It is not 
very functional at the moment, but soon I will modify this code to do 
something useful. 

The .xm File Format:

This project will implement the .xm file format, commonly used in 'demoscene'
music (visit https://modarchive.org/ for more info). The following files 
demonstrate the beginning of this implementation. More resources on this 
format will be made available in this repository shortly.

music_module.py:

This file contains work-in-progress code that creates musical pattern data
loosely based around the .xm file format.

musical_spelling.py:

This file contains work-in-progress code for converting human readable musical
spellings as integer sets, as in musical serialism. This code will be the basis
of a musical calculator, which will be able to quickly produce practical 
information about musical figures.

xm_header.py:

This file contains work-in-progress code that displays information from .xm
file headers. The basic usage is: python xm_header.py <filename>. Please note
that currently there is a bug that prevents most of this data from being 
displayed in the correct format.

xm_header_test.sh:

This is a bash script that opens multiple files with xm_header.py. The files 
need to be in a folder called xm-songs.