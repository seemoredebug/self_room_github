package com.example.selfroom.mappers;

import com.example.selfroom.bean.SeatInformation;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface SeatInformationMapper {
    public List<SeatInformation> getSeatInformation(String room);
}
