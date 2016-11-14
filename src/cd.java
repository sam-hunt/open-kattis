package kattis_java;

import java.util.Scanner;

public class cd {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextInt()) {
			int N = sc.nextInt(), M = sc.nextInt();
			if ((N == 0) && (M == 0)) {
				break;
			}
			
			int bothCount = 0, jill_cd = 0, pos = 0;
			int[] jack_collection = new int[M];
			
			for (int i=0; i<N; i++) {
				jack_collection[i] = sc.nextInt();
			}
			for (int i=0; i<M; i++) {
				jill_cd = sc.nextInt();
				try {
					if (jill_cd > jack_collection[M-1]) {
						throw new IndexOutOfBoundsException();
					}
					if (jill_cd < jack_collection[pos]) {
						continue;
					}
					if (jill_cd == jack_collection[pos]){
						bothCount++;
						pos++;
						continue;
					}
					
					while (jill_cd > jack_collection[pos]) {
						pos++;
					}
				} catch (java.lang.IndexOutOfBoundsException e) {
					for (int j=0; j<M-i; j++){
						sc.nextLine();
					}
					break;
				}
			}
			System.out.println(bothCount);
		}
	}

}
