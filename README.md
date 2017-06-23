# ldaPython
LDA Topic Analysis in Python

## Overview
I built off of [Jordan Barber's script](https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html) to do LDA in python.

The script takes a single column csv where each row is a document, checks for language (to insure it runs on english) and then runs an LDA Analysis on it.

A dummy example dataset of revolutionary slogans from the DPRK is included to give the script a test run.

## To Do List
- create a list of exempt words to filter out (currently has stop words but there may be unique words for each set of documents)
- choose the language to run the analysis on by looking at language frequency
- user input to set variables in the LDA itself and in other spots (like which document to use)




