package com.example.selfroom.mappers;


import com.example.selfroom.bean.RoomData;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface RoomDataMapper {
    public List<RoomData> getRoomData(String floor);
    public List<RoomData> getAllRoomData();
}
