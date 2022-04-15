package com.example.selfroom.test;


import com.example.selfroom.service.CmdService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class Cmdtest {
    @Autowired
    CmdService cmdService;
    @Test
    public void cmdtest(){
        System.out.println(cmdService.doFaceInMySql("all_faceDatas/190308010333-1.jpg","190308010333")); //all_faceDatas/190308010333-1.jpg  190308010333
    }
}
