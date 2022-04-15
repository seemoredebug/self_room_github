package com.example.selfroom.service;

import com.example.selfroom.bean.USerAppointment;
import com.example.selfroom.bean.UserDataROOT;
import com.example.selfroom.mappers.USerAppointmentMapper;
import com.example.selfroom.mappers.UserDataMapper;
import com.example.selfroom.bean.UserData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

@Service
public class UserDataService {
    @Autowired
    UserDataMapper userDataMapper;
    @Autowired
    GetNullListService getNullListService;

    public UserData getUserdata(String score){ return userDataMapper.getuserData(score);
    }//账号信息

    public List<UserDataROOT> getAllUserData(int page){//获得所有

            List<UserDataROOT> stu=userDataMapper.getAllUserData();
            int first=(page-1)*10;
            int end;
            if(stu.size()-first<10)
                end=stu.size()-first;
            else
                end=page*10;
            try {
            return stu.subList(first,end);
        }catch (Exception e){
                List<UserDataROOT> err=getNullListService.getNullUserDataROOTList();
            return err;
        }

    }
    public int countAllUserData(){
        return userDataMapper.countAllUserData();
    }

    public  String findPassword(String score){
        return userDataMapper.findpassword(score);
    }
    public boolean DeleteAll(String grade,String password,String score){
        try {
            if (userDataMapper.findpassword(score).equals(password))
            { String sqlgrade=grade+"%";
                userDataMapper.DeleteAll(sqlgrade);}
            return true;
        }catch (Exception e){
            return false;
        }

    }
    public  boolean DeleteOne(String score){
        try {
            userDataMapper.DeleteOne(score);
            return true;
        }catch (Exception e){
            return false;
        }

    }
    @Autowired
    USerAppointmentMapper uSerAppointmentMapper;

    public List<USerAppointment> getdata(String score, int page){//预约信息
        List<USerAppointment> stu=uSerAppointmentMapper.getUSerAppointment(score);
        int first=(page-1)*10;
        int end;
        if(stu.size()-first<10)
            end=stu.size()-first;
        else
            end=page*10;
        try {
        return stu.subList(first,end);
        }catch (Exception e){
            List<USerAppointment> err=getNullListService.getNullUSerAppointmentList();
            return err;
        }
    }
     public int countUSerAppointment(String score){
        return uSerAppointmentMapper.countUSerAppointment(score);
    }

    public List<USerAppointment> getNodata(String score,int page){//没去预约信息
        List<USerAppointment> stu=uSerAppointmentMapper.getNoUSerAppointment(score);
        int first=(page-1)*10;
        int end;
        if(stu.size()-first<10)
            end=stu.size()-first;
        else
            end=page*10;
        try{
        return stu.subList(first,end);
        }catch (Exception e){
            List<USerAppointment> err=getNullListService.getNullUSerAppointmentList();
            return err;
        }

    }
    public int countNoUSerAppointment(String score){
        return  uSerAppointmentMapper.countNoUSerAppointment(score);
    }


    public  boolean deleNoUSerAppointment(String number){
        if(uSerAppointmentMapper.getoUSerAppointmentBynumber(number).getUsed()==-1) {
            uSerAppointmentMapper.deleNoUSerAppointment(number);
            return true;
        }
        else
            return false;
    }
    public  USerAppointment getoUSerAppointmentBynumber(String number){
        return uSerAppointmentMapper.getoUSerAppointmentBynumber(number);
    }


}
