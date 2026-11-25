#!/bin/bash
# mkvid.sh outdir.mp4 img1 img2 ...
out=$1; shift; n=$#; D=3.2; X=0.5
args=(); f=""; i=0
for im in "$@"; do
  args+=(-framerate 30 -loop 1 -t $D -i "$im")
  f+="[$i:v]scale=1188:2112,zoompan=z='min(zoom+0.0006,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,trim=duration=$D,setpts=PTS-STARTPTS[v$i];"
  i=$((i+1))
done
prev="v0"; off=0
for ((k=1;k<n;k++)); do
  off=$(python3 -c "print(round($k*($D-$X),2))")
  f+="[$prev][v$k]xfade=transition=fade:duration=$X:offset=$off[x$k];"; prev="x$k"
done
f=${f%;}
ffmpeg -loglevel error -y "${args[@]}" -filter_complex "$f" -map "[$prev]" -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 23 -r 30 "$out"
