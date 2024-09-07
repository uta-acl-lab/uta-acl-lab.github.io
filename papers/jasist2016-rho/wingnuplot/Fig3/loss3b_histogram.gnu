set output "loss7.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25' size 6,4 lw 2
set key right 
#set boxwidth 1 absolute
set style fill solid border -1
set style data histogram
set style histogram cluster gap 2
set ytics nomirror
set xtics ("POS" 0, "WV" 1, "Retail" 2, "Syn" 3)
set yrange [0:1.0]
# set style line 1 lt 1 lw 2 pt 7 ps 1.5
# set style line 2 lt 2 lw 2 pt 8 ps 1.5
set xlabel "Data Sets"
set ylabel "Info Loss"
plot 'loss3b.dat' using 2  title "TDControl" fs pattern 0 lt -1,\
'loss3b.dat' using 3 title "Global" fs pattern 1 lt -1,\
'loss3b.dat' using 4 title "Mine" fs pattern 2 lt -1,\
'loss3b.dat' using 5 title "Dist" fs pattern 3 lt -1
