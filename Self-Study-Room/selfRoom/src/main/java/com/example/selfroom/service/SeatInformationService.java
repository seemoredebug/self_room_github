package com.example.selfroom.service;

import com.example.selfroom.bean.*;
import com.example.selfroom.mappers.BuildDataMapper;
import com.example.selfroom.mappers.RoomDataMapper;
import com.example.selfroom.mappers.SeatInformationMapper;
import com.example.selfroom.mappers.UsageRecordMapper;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SeatInformationService {

    @Autowired
    private SeatInformationMapper seatInformationMapper;

    public List<SeatInformation> getSeatInformation(String room){//每个房间的座位
        return seatInformationMapper.getSeatInformation(room);
    };

    @Autowired
    private RoomDataMapper roomDataMapper;

    public List<RoomData> getRoomData(String floor){//获取某一层
        return roomDataMapper.getRoomData(floor);
    }
    public List<RoomData> getAllRoomData(){//获取所有
        return roomDataMapper.getAllRoomData();
    }

    @Autowired
    private UsageRecordMapper usageRecordMapper;

     public List<UsageRecord> getUsageRecord(String room){//使用记录
         room+="%";
         return usageRecordMapper.getUsageRecord(room);
     }
     public int getOneUsageRecord(String recordNumber){//获取一条使用记录
         return  usageRecordMapper.getOneUsageRecord(recordNumber);
     }
     public void insertUsageRecord(UsageRecord usageRecord)//插入
     {
         usageRecordMapper.insertUsageRecord(usageRecord);
     }
     public  void  dropUsageRecord(UsageRecord usageRecord){//删除
         usageRecordMapper.dropUsageRecord(usageRecord);
     }

     @Autowired
    private BuildDataMapper buildDataMapper;
    public List<BuildData> getBuildData(int floor){
        return  buildDataMapper.getBuildData(floor);
    }

}
