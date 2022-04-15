package com.example.selfroom.control;

import com.example.selfroom.bean.USerAppointment;
import com.example.selfroom.bean.UserDataROOT;
import com.example.selfroom.mappers.UserDataMapper;
import com.example.selfroom.bean.UserData;
import com.example.selfroom.service.UserDataService;

import org.apache.commons.io.FileUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.Base64Utils;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;



import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.UUID;

@RestController
public class UserDataControl {

    @Autowired
    UserDataService userDataService;


    @RequestMapping("/stubase") //基本信息
    public UserData getUserData(String score){
        return userDataService.getUserdata(score);
    }

    @RequestMapping("/Allstubase")
    public List<UserDataROOT> getAllUserData(int page){//获得所有
        return userDataService.getAllUserData(page);
    }

    @RequestMapping("/AllstubaseC")
    public int countAllUserData(){
        return userDataService.countAllUserData();
    }

    @RequestMapping("/stuRese")  //预约信息
    public List<USerAppointment> getUSerAppointment(String score,int page){
        return userDataService.getdata(score,page);
    }

    @RequestMapping("/stuReseC")//预约信息数量
    public int countUSerAppointment(String score){
        return userDataService.countUSerAppointment(score);
    }

    @RequestMapping("/stuNoRese")  //没去预约信息
    public List<USerAppointment> getNoUSerAppointment(String score,int page){
        return userDataService.getNodata(score,page);
    }

    @RequestMapping("/stuNoReseC")//没去的数量
    public int countNoUSerAppointment(String score){
        return  userDataService.countNoUSerAppointment(score);
    }

    @RequestMapping("/stuDeleNoRese")  //删除没去预约信息
    public boolean deleNoUSerAppointment(String number){
         return  userDataService.deleNoUSerAppointment(number);
    }

    @RequestMapping("/stuDeleAll") //删除所有
    public boolean DeleteAll(String grade,String password,String score){
        return userDataService.DeleteAll(grade,password,score);
    }

    @RequestMapping("/stuDeleOne") //删除一个
    public boolean DeleteOne(String score){
         return userDataService.DeleteOne(score);
    }
    @RequestMapping("/stulogin") //登录密码验证
    public int stuLogin(String score,String password){
        if(userDataService.findPassword(score).equals(password)){
            return 1;
        }
        return -1;
    }
}
