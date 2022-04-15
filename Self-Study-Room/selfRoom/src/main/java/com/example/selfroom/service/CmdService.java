package com.example.selfroom.service;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.io.IOException;

@Service
@Async("CMDExecutor")
public class CmdService {
    public String doFaceInMySql(String fileurl,String score){
        //face_inMySqlAPI.exe all_faceDatas/190308010333-1.jpg  190308010333
        String c="face_inMySqlAPI.exe ";
        c+=fileurl;
        c+=" ";
        c+=score;
        try {

            Process process=Runtime.getRuntime().exec(c);
            return  "true";
        }catch (Exception e){
            return e.getMessage();
        }

    }
}
