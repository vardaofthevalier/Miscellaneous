import java.util.Scanner;

public class StringToLong {

	public static long ConvertStringToLong(String s)
	{
		long result = 0;
		
		long maxVal = (long) Math.pow(2, 63) - 1;
		long minVal = (long) Math.pow(2, 63) * (-1);
		
		// Boolean flag used to determine whether to use the signed or unsigned representation
		boolean isSigned = false;
		int maxLength = 20; // get rid of this later
		
		if (s.startsWith("-"))
		{
			// Use the signed representation ((-2^63), (2^63) -1) to represent negative integers
			isSigned = true;
		}
		else
		{
			// Use the unsigned representation (0, (2^64) -1) to represent positive integers
			isSigned = false;
		}
		
		if (s.length() > maxLength)
	    {
			// The number contained within s is too big
			// This is not a strict enough upper bound on the number of strings to reject.  This will still accept numbers of the appropriate length, 
			// with the last digit being greater than what it should be, and the overflow will still occur
			
			System.out.println("The string you entered is either too large or small to be represented as a signed 64-bit integer.");
			result = (Long) null;  // I just have a feeling this won't work...
		}
		else if (s.length() == maxLength)
		{
			// Here we need to check that the last digit doesn't exceed the value that its supposed to
			
			
		}
		else
		{
			int start = 1;
			int stop = s.length();
			int maxPower = s.length() - 2;
			
			if (!isSigned)
			{
				start = 0;
				maxPower = s.length() - 1;
			}
			
			while (start < stop)
			{
				int asciiVal = (int)s.charAt(start);
				
				if (asciiVal >= 48 && asciiVal <= 57)
				{
					long newValue = result + ((asciiVal - 48) * (long)Math.pow(10, maxPower));
					result = newValue;
				}
				else
				{
					System.out.println("The string you entered contains non-digit characters.");
					result = (Long) null;
				}
				maxPower -= 1;
				start += 1;
			}
		}
		
		if (isSigned)
		{
			// we are dealing with a negative number
			result = result*(-1);
		}
		return result;
	}
	public long decimalToBinary(String s)
	{
		int leftEnd = 0;
		int rightEnd = s.length() - 1;
		int maxPower = s.length() - 2;
		
		long binaryTotal = 0b0;
		long power = 0;
		
		while (rightEnd > leftEnd)
		{
			int asciiVal = (int)s.charAt(rightEnd);
			
			if (asciiVal >= 48 && asciiVal <= 57)
			{
				int digitValue = result + ((asciiVal - 48) * (int)Math.pow(10, maxPower));
			}
			else
			{
				System.out.println("The string you entered contains non-digit characters.");
				System.exit(-1);
			}
			
			if (digitValue < 2)
			{
				try
				{
					binaryTotal += 0b1;
				}
				catch ??
				{
					// Here is where we should catch the overflow
				}
				return binaryTotal;
			}
			else
			{
				if (Math.floor(digitValue/2) != 1)
				{
					power += decimalToBinary(ToString(floor(digitValue/2));
				}
				else
				{
					power = decimalToBinary(ToString(digitValue - 
				}
			}
			rightEnd--;
			
		}
	}
	
	public static void main(String[] args) {
		
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Enter a number to be stored as a string: ");
		String s = keyboard.nextLine();
		keyboard.close();
		
		// Find what the long value should be
		long l = (Long)null;
		
		try
		{
			l = Long.parseLong(s);
			System.out.println("The built-in conversion function returns a long with this value: " + l);
		}
		catch (NumberFormatException e)
		{
			System.out.println("The built-in conversion function can't represent that number as a long, so mine probably shouldn't, either.");
		}
		
		long converted = ConvertStringToLong(s);
		
		if (converted != (Long)null)
		{
			System.out.println("My implementation of the conversion function returns a long value of: " + converted);
			
			if (converted == l)
			{
				System.out.println("The string was successfully converted!");
			}
			else
			{
				System.out.println("The string was NOT successfully converted.");
			}
		}

	}

}

