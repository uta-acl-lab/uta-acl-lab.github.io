#!/usr/bin/gnuplot

reset

# epslatex
set terminal postscript eps size 3.5,2.62 enhanced color \
    font 'Times, 18' linewidth 2
set output 'differentn.eps'

# color definitions
# set border linewidth 1.5
set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 2 ps 1 # --- blue
set style line 2 lc rgb '#dd181f' lt 1 lw 2 pt 5 ps 1 # --- red
set style line 3 lc rgb '#00ff00' lt 1 lw 2 pt 8 ps 1 # --- green
set style line 4 lc rgb '#ff6600' lt 1 lw 2 pt 6 ps 1 # --- orange
set style line 5 lc rgb '#009900' lt 1 lw 2 pt 7 ps 1 # --- black
set style line 6 lc rgb '#669999' lt 1 lw 2 pt 8 ps 1 # --- black
set style line 7 lc rgb '#000000' lt 1 lw 2 pt 8 ps 1 # --- black

#set style line 4 lc rgb '#000000' dashtype 2 lw 2 

set xlabel 'Number of document clusters, N'
set ylabel "Total Loss"
set grid ytics lc rgb "#bbbbbb" lw 1 lt 0
set grid xtics lc rgb "#bbbbbb" lw 1 lt 0

# set ytics 1
# set tics scale 0.75

set xtics 1

set xrange [5:14]
set yrange [0.0:10.0]

plot 'differentn.txt' index 0 with linespoints ls 1 t ""