function [ Imim] = intensitet( filnavn )
I = imread(filnavn);
Imim = mean(I,1);
imagesc(I);
end



