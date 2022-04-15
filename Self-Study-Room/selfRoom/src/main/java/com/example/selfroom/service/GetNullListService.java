package com.example.selfroom.service;

import com.example.selfroom.bean.USerAppointment;
import com.example.selfroom.bean.UserDataROOT;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

@Service
public class GetNullListService {

   public List<UserDataROOT>  getNullUserDataROOTList(){
       List<UserDataROOT> err=new List<UserDataROOT>() {
           @Override
           public int size() {
               return 0;
           }

           @Override
           public boolean isEmpty() {
               return false;
           }

           @Override
           public boolean contains(Object o) {
               return false;
           }

           @Override
           public Iterator<UserDataROOT> iterator() {
               return null;
           }

           @Override
           public Object[] toArray() {
               return new Object[0];
           }

           @Override
           public <T> T[] toArray(T[] a) {
               return null;
           }

           @Override
           public boolean add(UserDataROOT userDataROOT) {
               return false;
           }

           @Override
           public boolean remove(Object o) {
               return false;
           }

           @Override
           public boolean containsAll(Collection<?> c) {
               return false;
           }

           @Override
           public boolean addAll(Collection<? extends UserDataROOT> c) {
               return false;
           }

           @Override
           public boolean addAll(int index, Collection<? extends UserDataROOT> c) {
               return false;
           }

           @Override
           public boolean removeAll(Collection<?> c) {
               return false;
           }

           @Override
           public boolean retainAll(Collection<?> c) {
               return false;
           }

           @Override
           public void clear() {

           }

           @Override
           public UserDataROOT get(int index) {
               return null;
           }

           @Override
           public UserDataROOT set(int index, UserDataROOT element) {
               return null;
           }

           @Override
           public void add(int index, UserDataROOT element) {

           }

           @Override
           public UserDataROOT remove(int index) {
               return null;
           }

           @Override
           public int indexOf(Object o) {
               return 0;
           }

           @Override
           public int lastIndexOf(Object o) {
               return 0;
           }

           @Override
           public ListIterator<UserDataROOT> listIterator() {
               return null;
           }

           @Override
           public ListIterator<UserDataROOT> listIterator(int index) {
               return null;
           }

           @Override
           public List<UserDataROOT> subList(int fromIndex, int toIndex) {
               return null;
           }
       };
       return err;
   }

   public List<USerAppointment> getNullUSerAppointmentList(){
       List<USerAppointment> err = new List<USerAppointment>() {
           @Override
           public int size() {
               return 0;
           }

           @Override
           public boolean isEmpty() {
               return false;
           }

           @Override
           public boolean contains(Object o) {
               return false;
           }

           @Override
           public Iterator<USerAppointment> iterator() {
               return null;
           }

           @Override
           public Object[] toArray() {
               return new Object[0];
           }

           @Override
           public <T> T[] toArray(T[] a) {
               return null;
           }

           @Override
           public boolean add(USerAppointment uSerAppointment) {
               return false;
           }

           @Override
           public boolean remove(Object o) {
               return false;
           }

           @Override
           public boolean containsAll(Collection<?> c) {
               return false;
           }

           @Override
           public boolean addAll(Collection<? extends USerAppointment> c) {
               return false;
           }

           @Override
           public boolean addAll(int index, Collection<? extends USerAppointment> c) {
               return false;
           }

           @Override
           public boolean removeAll(Collection<?> c) {
               return false;
           }

           @Override
           public boolean retainAll(Collection<?> c) {
               return false;
           }

           @Override
           public void clear() {

           }

           @Override
           public USerAppointment get(int index) {
               return null;
           }

           @Override
           public USerAppointment set(int index, USerAppointment element) {
               return null;
           }

           @Override
           public void add(int index, USerAppointment element) {

           }

           @Override
           public USerAppointment remove(int index) {
               return null;
           }

           @Override
           public int indexOf(Object o) {
               return 0;
           }

           @Override
           public int lastIndexOf(Object o) {
               return 0;
           }

           @Override
           public ListIterator<USerAppointment> listIterator() {
               return null;
           }

           @Override
           public ListIterator<USerAppointment> listIterator(int index) {
               return null;
           }

           @Override
           public List<USerAppointment> subList(int fromIndex, int toIndex) {
               return null;
           }
       };
       return err;
   }
}
