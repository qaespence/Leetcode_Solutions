using System;

namespace LeetCode
{
    class DefangingAnIpAddress
    {
        public String DefangingAnIpAddressSolution(String address)
        {
            var result = "";
            foreach(char character in address)
            {
                if(character == '.')
                {
                    result += "[.]";
                }
                else
                {
                    result += character;
                }
            }

            return result;
        }
    }
}
