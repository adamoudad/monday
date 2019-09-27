% Coursera - Machine Learning
% Linear Regression With Multiple Variables (Quizz notes)

X = [89 7921 ;72 5184 ;94 8836 ;69 4761];
y = [96; 74 ; 87 ; 78];
i = 2 % feature #
j = 2 % sample #
xi_max = max(X(:,i));
xi_min = min(X(:,i));
range = xi_max - xi_min;
disp((X(2,i) - mean(X(:,i))) / range);


function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

  % Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
for iter = 1:num_iters,
    disp(computeCost(X,y,theta))
    updates = - alpha * (X * theta - y)' * X / m
    theta += updates'
    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end
end
