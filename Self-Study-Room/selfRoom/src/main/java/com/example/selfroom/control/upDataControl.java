package com.example.selfroom.control;

import com.example.selfroom.mappers.TestMapper;
import com.example.selfroom.service.CmdService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

@RestController
public class upDataControl {

    @Autowired
    CmdService cmdService;
//    SimpleDateFormat sd = new SimpleDateFormat("yyyy/MM/dd");

    @PostMapping("/uploadImg")
    public String uploadImg(MultipartFile uploadFile, HttpServletRequest req) {
        //获取文件名
        String fileName = uploadFile.getOriginalFilename();
        //获取文件后缀名
        String suffixName = fileName.substring(fileName.lastIndexOf("."));
        //重新生成文件名
//        fileName = UUID.randomUUID()+suffixName;
        //添加日期目录
//        String format = sd.format(new Date());
        //指定本地文件夹存储图片
        String filePath = "all_faceDatas" + "/";
        String rootPath = "/home/java/";
        File file = new File(filePath, fileName);
        if (!file.getParentFile().exists()) {
            file.getParentFile().mkdirs();
        }
        try {
            //将图片保存到static文件夹里
            boolean fb = file.createNewFile();
            if (fb)
                System.out.println("NO");
            else
                System.out.println("YES");
            uploadFile.transferTo(new File(rootPath + filePath + fileName));
            System.out.println(filePath + fileName);
            System.out.println(fileName.substring(0, 12));
            cmdService.doFaceInMySql(filePath + fileName, fileName.substring(0, 12));
            return "http://" + req.getRemoteHost() + ":" + req.getServerPort() + "/" + fileName;
        } catch (Exception e) {
            e.printStackTrace();
            return "false";
        }
    }

    @Autowired
    TestMapper testMapper;
    @RequestMapping("/test")
    public String cmd(String score){
        try{

            return testMapper.getTest(score);
        }catch (Exception e){
            return e.getMessage();
        }
    }
}
