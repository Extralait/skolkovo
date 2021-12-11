using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public static class ValidationClass
    {
        public static bool Check(List<AuthInfo> authInfoList, AuthInfo newAuthInfo, int coefficient)
        {
            if (authInfoList.Count < 1)
                return true;
            bool flag = false;
            foreach (AuthInfo authInfo in authInfoList)
            {
                int num1 = 0;
                if (newAuthInfo.City == authInfo.City)
                    ++num1;
                if (newAuthInfo.Country == authInfo.Country)
                    ++num1;
                if (newAuthInfo.DesktopResolution == authInfo.DesktopResolution)
                    ++num1;
                if (newAuthInfo.Ip == authInfo.Ip)
                    ++num1;
                if (newAuthInfo.Login == authInfo.Login)
                    ++num1;
                if (newAuthInfo.OS == authInfo.OS)
                    ++num1;
                if (newAuthInfo.StateProv == authInfo.StateProv)
                    ++num1;
                if (newAuthInfo.Token == authInfo.Token)
                    ++num1;
                if (newAuthInfo.UserAgent == authInfo.UserAgent)
                    ++num1;
                if (newAuthInfo.VideoCard == authInfo.VideoCard)
                    ++num1;
                int num2 = num1 * 100 / 10;
                if (num2 >= coefficient)
                {
                    flag = true;
                    Console.WriteLine(string.Format("Совпадение = {0}", (object)num2));
                    break;
                }
            }
            if (!flag)
                Console.WriteLine("НЕТ СОВПАДЕНИЯ !");
            return flag;
        }
    }
}
