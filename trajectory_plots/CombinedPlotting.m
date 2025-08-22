
size = 18;

fig = figure;

subplot(3,5,1)
set(gcf,'color','white');
plot(-StylusPositionX_hex_Off,StylusPositionY_hex_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_hex_Off(:,1),new_vertices_hex_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,2)
set(gcf,'color','white');
plot(-StylusPositionX_tri_Off,StylusPositionY_tri_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_tri_Off(:,1),new_vertices_tri_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,3)
set(gcf,'color','white');
plot(-StylusPositionX_cir_Off,StylusPositionY_cir_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_cir_Off(:,1),new_vertices_cir_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);
title('(a) Patient Unassisted','HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');

subplot(3,5,4)
set(gcf,'color','white');
plot(-StylusPositionX_inf_Off,StylusPositionY_inf_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_inf_Off(:,1),new_vertices_inf_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,5)
set(gcf,'color','white');
plot(-StylusPositionX_B_Off,StylusPositionY_B_Off,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_B_Off(:,1),new_vertices_B_Off(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,6)
set(gcf,'color','white');
plot(-StylusPositionX_hex_On,StylusPositionY_hex_On,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_hex_On(:,1),new_vertices_hex_On(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,7)
set(gcf,'color','white');
plot(-StylusPositionX_tri_On,StylusPositionY_tri_On,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_tri_On(:,1),new_vertices_tri_On(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,8)
set(gcf,'color','white');
plot(-StylusPositionX_cir_On,StylusPositionY_cir_On,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_cir_On(:,1),new_vertices_cir_On(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);
title('(b) Patient Assisted','HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');


subplot(3,5,9)
set(gcf,'color','white');
plot(-StylusPositionX_inf_On,StylusPositionY_inf_On,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_inf_On(:,1),new_vertices_inf_On(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,10)
set(gcf,'color','white');
plot(-StylusPositionX_B_On,StylusPositionY_B_On,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_B_On(:,1),new_vertices_B_On(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,11)
set(gcf,'color','white');
plot(-StylusPositionX_hex,StylusPositionY_hex,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_hex(:,1),new_vertices_hex(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,12)
set(gcf,'color','white');
plot(-StylusPositionX_tri,StylusPositionY_tri,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_tri(:,1),new_vertices_tri(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,13)
set(gcf,'color','white');
plot(-StylusPositionX_cir,StylusPositionY_cir,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_cir(:,1),new_vertices_cir(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);
title('(c) Healthy','HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');

subplot(3,5,14)
set(gcf,'color','white');
plot(-StylusPositionX_inf,StylusPositionY_inf,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_inf(:,1),new_vertices_inf(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);


subplot(3,5,15)
set(gcf,'color','white');
plot(-StylusPositionX_B,StylusPositionY_B,'color','#DD6236','LineWidth',2);
hold on;
plot(new_vertices_B(:,1),new_vertices_B(:,2),'color','#0068CA','LineWidth',4);
set(gca,'FontSize',size,'FontName', 'Times New Roman','fontweight','bold','linewidth',1.5);

legend('Subject','Reference');


han=axes(fig,'visible','off'); 
han.Title.Visible='on';
han.XLabel.Visible='on';
han.YLabel.Visible='on';
xlabel(han,'X-coordinate (mm)','FontName', 'Times New Roman','FontSize',20);
ylabel(han,'Y-coordinate (mm)','FontName', 'Times New Roman','FontSize',20);
