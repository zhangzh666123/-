package com.orange.View;
 
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
 
import com.orange.Controller.Select;
import com.orange.Controller.Updata;
import com.orange.Utils.ValidateUtils;
 
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.awt.event.ActionEvent;
import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.Toolkit;
 
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.ImageIcon;
 
//添加图书界面
 
public class Registration_Info extends JFrame {
 
	private static final long serialVersionUID = 1L;
 
	private JTextField nameField;
	private JTextField ageField;
	private JTextField IDcardField;
	private JTextField addressField;
	private JTextField phoneField;
	private JTextField touristNumberField;
	private JTextField accompanyField;
	private JTextField foodsField;
	Select select = new Select();
	Updata updata = new Updata();
	String name,sex,age,IDcard,address,phone,touristNumber,accompany,foods;
 
	public Registration_Info() {
 
		super("填写图书信息");
		this.setBounds(0, 0, 800, 600);
		this.setLocationRelativeTo(null);//让窗口在屏幕中间显示
		this.setResizable(false);//让窗口大小不可改变
		getContentPane().setLayout(null);
		
		//设置窗口图标
	    Toolkit tk = Toolkit.getDefaultToolkit();
	    Image frameImage=tk.createImage("img/logo.png"); 
	    this.setIconImage(frameImage);
		
	    //图片添加
        JLabel jl = new JLabel();
        jl.setIcon(new ImageIcon("img/brand.png"));//文件路径
        jl.setBounds(453, 10, 800, 300);
        this.add(jl);
	    
        //书名
		JLabel nameLabel= new JLabel("书   名：");
		nameLabel.setFont(new Font("微软雅黑", Font.BOLD, 15));
		nameLabel.setBounds(130, 39, 72, 18);
		getContentPane().add(nameLabel);
		
		nameField = new JTextField();
		nameField.setBounds(191, 36, 240, 28);
		getContentPane().add(nameField);
		nameField.setColumns(10);
		
 
		
		//编码
		JLabel ageLabel= new JLabel("编   码：");
		ageLabel.setFont(new Font("微软雅黑", Font.BOLD, 15));
		ageLabel.setBounds(130, 138, 72, 18);
		getContentPane().add(ageLabel);
		
		ageField = new JTextField();
		ageField.setBounds(191, 135, 240, 28);
		getContentPane().add(ageField);
		ageField.setColumns(10);
		
		//图书代码
		JLabel IDcardLabel= new JLabel("图书代码：");
		IDcardLabel.setFont(new Font("微软雅黑", Font.BOLD, 15));
		IDcardLabel.setBounds(98, 188, 117, 18);
		getContentPane().add(IDcardLabel);
		
		IDcardField = new JTextField();
		IDcardField.setBounds(191, 185, 240, 28);
		getContentPane().add(IDcardField);
		IDcardField.setColumns(10);
		
		//作者信息
		JLabel addressLabel= new JLabel("作者信息：");
		addressLabel.setFont(new Font("微软雅黑", Font.BOLD, 15));
		addressLabel.setBounds(113, 234, 100, 18);
		getContentPane().add(addressLabel);
		
		addressField = new JTextField();
		addressField.setBounds(191, 231, 240, 28);
		getContentPane().add(addressField);
		addressField.setColumns(10);
		
		//出版方
		JLabel phoneLabel= new JLabel("出版方：");
		phoneLabel.setFont(new Font("微软雅黑", Font.BOLD, 15));
		phoneLabel.setBounds(113, 280, 100, 18);
		getContentPane().add(phoneLabel);
		
		phoneField = new JTextField();
		phoneField.setBounds(191, 277, 240, 28);
		getContentPane().add(phoneField);
		phoneField.setColumns(10);
		
 
		//立即报名
		JButton submitButton = new JButton("立即添加");
		submitButton.setFont(new Font("微软雅黑", Font.PLAIN, 18));
		submitButton.setBounds(320, 495, 150, 33);
		submitButton.setFocusPainted(false);//去掉按钮周围的焦点框
		submitButton.setBackground(new Color(78, 110, 242));
		submitButton.setForeground(Color.WHITE);
		getContentPane().add(submitButton);
		
		submitButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
 
				//判断输入的信息是否为空，是否完整
				if (name.equals("")||sex.equals("")||age.equals("")||IDcard.equals("")||address.equals("")||phone.equals("")||touristNumber.equals("")||accompany.equals("")||foods.equals("")) {
					JOptionPane.showMessageDialog(null, "请输入完整信息！");
				} else {
					//判断身份证号码
					if (!ValidateUtils.IDcard(IDcard)) {
						JOptionPane.showMessageDialog(null, "身份证号码错误！请检查！");
					} else {
						String i = select.getString("SELECT user_id FROM `user` WHERE user_state='已登录'");
						String sql = "INSERT INTO `tourist` VALUES (null, '"+i+"', '"+name+"', '"+sex+"', '"+age+"', '"+IDcard+"', '"+address+"', '"+phone+"', '"+touristNumber+"', '"+accompany+"', '"+foods+"');";
						int result = updata.addData(sql);
						//判断手机号是否符合格式
						String regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(17[013678])|(18[0,5-9]))\\d{8}$";
				        if(phone.length() != 11){
				        	JOptionPane.showMessageDialog(null, "手机号应为11位数！");
				        }else{
				            Pattern p = Pattern.compile(regex);
				            Matcher m = p.matcher(phone);
				            boolean isMatch = m.matches();
				            if(!isMatch){
				                JOptionPane.showMessageDialog(null, "您的手机号" + phone + "是错误格式！！！");
				            }else {
				            	//判断插入结果
				            	if (result>0) {
				            		JOptionPane.showMessageDialog(null, "报名成功！");
				            		dispose();//关闭窗口
				            	} else {
				            		JOptionPane.showMessageDialog(null, "报名失败，请与管理员联系！");
				            	}
							}
				        }
					}
				}
			}
		});
		
	}
}
