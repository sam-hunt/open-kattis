package kattis_java;

import java.util.Scanner;
import java.math.BigInteger;

public class listgame {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		BigInteger X = sc.nextBigInteger();
		
		if (X.isProbablePrime(10)) {
			System.out.println("1");
		}
		
		int pfactors = 0;
		BigInteger i = 2;
		BigInteger two = BigInteger.ONE.add(BigInteger.ONE);
		BigInteger i = new BigInteger(two);
		while (X.compareTo(two) > 0) {
			if ((X.mod(i)) == BigInteger.ZERO) {
				
			}
		}
	}

}
