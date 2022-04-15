package com.example.selfroom.mappers;

import com.example.selfroom.bean.UserData;
import com.example.selfroom.bean.UserDataROOT;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface UserDataMapper {
    public UserData getuserData(String score);
    void DeleteAll(String grade);
    void DeleteOne(String score);
    String findpassword(String score);
    public List<UserDataROOT> getAllUserData();
    public int countAllUserData();
}
