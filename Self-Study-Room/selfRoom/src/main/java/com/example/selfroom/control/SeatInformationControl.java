package com.example.selfroom.control;

import com.example.selfroom.bean.BuildData;
import com.example.selfroom.bean.RoomData;
import com.example.selfroom.bean.SeatInformation;
import com.example.selfroom.bean.UsageRecord;
import com.example.selfroom.service.SeatInformationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class SeatInformationControl {

    @Autowired
    SeatInformationService seatInformationService;

    @RequestMapping("/login")
//    @GetMapping()
    public String getlogin(String username,String password){
        return "hello";
    }

    @RequestMapping("/seat")//每个房间的座位位置
    public List<SeatInformation> getSeatInformation(String room){
        return seatInformationService.getSeatInformation(room);
    }

    @RequestMapping("/room")//获取某一层余量
    public List<RoomData> getRoomData(String floor){
        return seatInformationService.getRoomData(floor);
    }

    @RequestMapping("/Allroom")
    public List<RoomData> getAllRoomData(){//获取所有房间余量
        return seatInformationService.getAllRoomData();
    }


    @RequestMapping("/seatrecord")//座位使用记录
    public List<UsageRecord> getUsageRecord(String room){
        return seatInformationService.getUsageRecord(room);
    }

    @RequestMapping("/build")//获取有哪几层一层多少房间
    public List<BuildData> getBuildData(int floor){
        return seatInformationService.getBuildData(floor);
    }
}
