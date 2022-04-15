package com.example.selfroom.bean;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class SeatInformation {
    private String seatNumber;
    private int seatAddressX;
    private int seatAddressY;
    private int used;
    private String roomNumber;
}
