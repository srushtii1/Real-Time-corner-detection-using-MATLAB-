%3160 Srushti Fulpagar IVA Project
clc
clear all
close all
warning off
c=webcam;
while true
e=c.snapshot;
imshow(e);
points=detectHarrisFeatures(rgb2gray(e));
se=selectStrongest(points,15);
hold on;
plot(se.Location(:,1),se.Location(:,2),'g.','MarkerSize',20);
drawnow;
hold off;
end