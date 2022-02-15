# Lab4

In this lab, we implemented a simple step-response for a first order circuit using
timer based interrupts.

The capacitor we used was 3.35 micro farads and the resistor was 51.1 kilo ohms.
This made the theoretical time constant (tau) 0.171185 seconds. The lab said that
we wanted to make a tau of about 0.3 seconds but we found that with one thousand
data points a smaller tau made the steady-state of the system more visible.

1[](51-1k.png)

Experimental Tau = 171.25 ms
Theoretical Tau = 171.185 ms
Percent Difference = 0.0038%

This difference is so small that we can conclude that we both did the experiment
correctly and probably got a little bit lucky.

The plot shown above has some annotations on it to show where it reached 63% and
86% of its max value, this way tau could be calculated. The points were found
using the matplotlib output and hovering over the graph but they were annotated
later for clarity.

Points of interest, (170, 1.99) one tau, (345, 2.72) two tau