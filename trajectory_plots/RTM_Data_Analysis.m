% path1 = [StylusPositionX,StylusPositionY];
% path2 = [TargetPositionX,TargetPositionY];
% 
% minDistance = inf;
% ShortestDistance = inf(size(StylusPositionX));
% 
% closestPoints = [];
% 
% % Calculate the distances between each point in path1 and each point in path2
% for i = 1:size(StylusPositionX)
%     for j = 1:size(TargetPositionX)
%         % Calculate the Euclidean distance
%         distance = sqrt((path1(i, 1) - path2(j, 1))^2 + (path1(i, 2) - path2(j, 2))^2);
%         % Check if this distance is the smallest so far
%         if distance < minDistance
%             minDistance = distance;
%     %       closestPoints = [path1(i, :); path2(j, :)]; % Store the closest points
%         end
%     end
%       ShortestDistance(i) = minDistance;  
% end
% 
% Average_deviation = mean(ShortestDistance);


% Define the two points
point1 = [x1, y1]; % First point (x1, y1)
point2 = [x2, y2]; % Second point (x2, y2)

% Generate 12 points including the start and end points
num_points = 12; % Total points (2 original points + 10 interpolated)
x_values = linspace(point1(1), point2(1), num_points);
y_values = linspace(point1(2), point2(2), num_points);

% Combine the interpolated points into a single array
interpolated_points = [x_values' y_values'];

% Display the interpolated points
disp('Interpolated Points:');
disp(interpolated_points);
