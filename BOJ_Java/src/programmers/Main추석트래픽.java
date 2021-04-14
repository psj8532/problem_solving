package programmers;

import java.util.LinkedList;
import java.util.List;

public class Main추석트래픽 {
	
	private static class Time {
		private double start, end;
		
		public void setTime(double start, double end) {
			this.start = start;
			this.end = end;
		}
		
		public double getStart() {
			return this.start;
		}
		
		public double getEnd() {
			return this.end;
		}
	}
	
	private static double changeTime(String s) {
		int hour, minute;
        double sec;
        String[] time = s.split(":");
        hour = Integer.parseInt(time[0]) * 3600;
        minute = Integer.parseInt(time[1]) * 60;
        sec = Double.parseDouble(time[2]);
        
        return hour + minute + sec;
	}
	
	private static int solution(String[] lines) {
        int answer = 0;
        String[] info;
        double start, end, processTime;
        
        List<Time> deq = new LinkedList<Time>();
        
        for(String information : lines) {
        	info = information.split(" ");
        	end = changeTime(info[1]);
        	processTime = Float.parseFloat(info[2].substring(0, info[2].length()-1));
        	start = Math.round((end - processTime + 0.001) * 1000) / 1000.0;
        	
        	Time time = new Time();
        	time.setTime(start, end);
        	deq.add(time);
        	
        }
        
        double s, e, compS;
        while (!deq.isEmpty()) {
        	Time time = deq.remove(0);
        	s = time.getStart();
        	e = time.getEnd();
        	int cnt = 1;
        	
        	for (Time t : deq) {
        		compS = t.getStart();
        		if (compS < e + 1) cnt ++;
        	}
        	
        	if (cnt > answer) answer = cnt;
        }
        return answer;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] ex = {
				"2016-09-15 01:00:04.001 2.0s",
				"2016-09-15 01:00:07.000 2s"
		};
		System.out.println(solution(ex));
	}

}
