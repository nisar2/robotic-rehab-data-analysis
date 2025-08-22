tiledlayout(2,2);

% Tile 1
nexttile
set(gcf,'color','white');
plot(-StylusPositionX_hex_Off,StylusPositionY_hex_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_hex_Off(:,1),new_vertices_hex_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',20,'FontName', 'Times New Roman','fontweight','bold','linewidth',2);

% Tile 2
nexttile
set(gcf,'color','white');
plot(-StylusPositionX_tri_Off,StylusPositionY_tri_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_tri_Off(:,1),new_vertices_tri_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',20,'FontName', 'Times New Roman','fontweight','bold','linewidth',2);

title('Row 1');

% Tile 3
nexttile
set(gcf,'color','white');
plot(-StylusPositionX_cir_Off,StylusPositionY_cir_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_cir_Off(:,1),new_vertices_cir_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',20,'FontName', 'Times New Roman','fontweight','bold','linewidth',2);

% Tile 4
nexttile
set(gcf,'color','white');
plot(-StylusPositionX_inf_Off,StylusPositionY_inf_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_inf_Off(:,1),new_vertices_inf_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',20,'FontName', 'Times New Roman','fontweight','bold','linewidth',2);

title('Row 2');
% 
% axgrid = [2,2];  % [#rows, #cols]
% titles = {'Row 1 title', 'Row 2 title'}; 

% tclMain = tiledlayout(axgrid(1),1); 
% tcl = gobjects(1,axgrid(1));
% ax = gobjects(axgrid); 
% for j = 1:numel(tcl)
%     tcl(j) = tiledlayout(tclMain,1,axgrid(2));
%     tcl(j).Layout.Tile = j; 
%     for i = 1:axgrid(2)
%         ax(j,i) = nexttile(tcl(j)); 
%     end
%     title(tcl(j),titles{j})
% end