% (AT)*A*(betta) = (AT)*y -> Normalligningen
% betta = inv(AT*A)*AT*y -> gir meg parametervektoren  
% y-vektor = observasjonsvektor
y = [
4.05
4.15
3.85
-0.22];
% x-vektor
x = [
0.08
0.12
0.20
0.38];

%Oppgave a)
X = zeros(4,3); %Designmatrise X

for i = 1:4
    X(i,:) = [1 x(i) x(i)^2];
end

XT = transpose(X);     %X-transponert
betta = inv(XT*X)*XT*y %Parametervektor

%% 
%Oppgave b)
A = zeros(4,2); %Designmatrise A

for i = 1:4
    A(i,:) = [sin(2*pi*x(i)) cos(2*pi*x(i))];
end

AT = transpose(A);     %A-transponert
alpha = inv(AT*A)*AT*y %Parametervektor
%% 


%% 
%Oppgave c)
Xbetta = X*betta;
Aalpha = A*alpha;
Epsi_X = zeros(4,1); %residualvektor for X
Epsi_A = zeros(4,1); %residualvektor for A
for i= 1:4
    Epsi_X(i) = y(i) - Xbetta(i);
    Epsi_A(i) = y(i) - Aalpha(i);
end

norm(Epsi_X), norm(Epsi_A)