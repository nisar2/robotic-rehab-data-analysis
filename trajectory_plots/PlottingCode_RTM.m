close all
clc

offset = Timestamp(1);
Timestamp_offset=zeros(size(Timestamp,1),1);
time=zeros(size(Timestamp,1),1);
time(1)=0;
ticks_per_sec = 10^7;


minDistance = inf;
Deviation = inf(size(StylusPositionX));
closestPoint = [];


% Extracting time in seconds from the Unity timestamp
for i=2:size(Timestamp,1)
    Timestamp_offset(i)=Timestamp(i)-offset;
    time=Timestamp_offset/(ticks_per_sec);
end

% Adding a last row to each target position coordinates, so that plotting
% connects last target to first target in a loop
% X(end+1)=X(1);
% Y(end+1)=Y(1);

% Converting target positions to haptic plugin units
TargetPositionX = -X*1000;
TargetPositionY = Y*1000;

Number_Targets = size(TargetPositionY,1);

StylPos = [-StylusPositionX,StylusPositionY];
TargPos = [TargetPositionX,TargetPositionY];

%% Adding points between targets for higher resolution

vertices = zeros(Number_Targets,2);

for i = 1:Number_Targets
    vertices(i,1) = TargetPositionX(i);
    vertices(i,2) = TargetPositionY(i);
end


% Number of interpolated points between each target
num_points = 10;

% Initialize the new vertices list
new_vertices = [];

% Loop through each edge of the trail
for i = 1:size(vertices, 1)
    % Get the current target
    p1 = vertices(i, :);
    
    % Get the next target (wrap around to the first vertex)
    p2 = vertices(mod(i, size(vertices, 1)) + 1, :);
    
    % Generate interpolated points between p1 and p2
    x_interp = linspace(p1(1), p2(1), num_points + 2);
    y_interp = linspace(p1(2), p2(2), num_points + 2);
    
    % Skip the last interpolated point (to avoid duplication)
    interpolated_points = [x_interp(1:end-1)', y_interp(1:end-1)'];
    
    % Add the interpolated points to the new vertices list
    new_vertices = [new_vertices; interpolated_points];
end

% Close the polygon by adding the first vertex at the end
new_vertices = [new_vertices; new_vertices(1, :)];


new_vertices_hex = new_vertices;
StylusPositionX_hex = StylusPositionX;
StylusPositionY_hex = StylusPositionY;


% Plot the original and interpolated trails
% 
% figure;
% set(gcf,'color','white');
% plot(vertices(:, 1), vertices(:, 2), 'ro-', 'LineWidth', 3);
% hold on;
% plot(new_vertices(:, 1), new_vertices(:, 2), 'b.-', 'LineWidth', 3);
% set(gca,'FontSize',40,'FontName', 'Times New Roman','fontweight','bold','linewidth',2);
% xlabel('X-coordinate (mm)','FontSize',50);
% ylabel('Y-coordinate (mm)','FontSize',50);
% legend('Targets');
% axis equal;
% % grid on;



%% Finding minimum distance for each stylus position to new_vertices

for i = 1 : size(StylusPositionX);
    for j = 1:size(new_vertices,1)
        % Calculate the Euclidean distance
        distance(j) = sqrt((StylPos(i, 1) - new_vertices(j, 1))^2 + (StylPos(i, 2) - new_vertices(j, 2))^2);

        % Check if this distance is the smallest so far
%         if distance < minDistance
%             minDistance = distance;
%             closestPoint = [new_vertices(j, :)]; % Store the closest point
%         end
    end
      minDistance = min(distance);
      Deviation(i,1) = minDistance;  
end


Average_deviation = mean(Deviation);
Total_time = time(end);


% Plotting target positions and human subject's positions
figure
set(gcf,'color','white');
plot(-StylusPositionX,StylusPositionY,'color',[0.87, 0.18, 0.18],'LineWidth',2);
hold on;
plot(new_vertices(:,1),new_vertices(:,2),'color','b','LineWidth',4);
set(gca,'FontSize',40,'FontName', 'Times New Roman','fontweight','bold','linewidth',2);
xlabel('X-coordinate (cm)','FontSize',50);
ylabel('Y-coordinate (cm)','FontSize',50);
legend('Reference','Subject');
% axis equal;


% Time for all loops
Total_time = time(end);


