using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        private static void Main(string[] args)
        {
            int coefficient = 70;
            List<AuthInfo> authInfoList = new List<AuthInfo>();
            authInfoList.Add(new AuthInfo()
            {
                City = "Samara",
                Country = "Russia",
                DesktopResolution = "1920*1024",
                Ip = "94.100.120.5",
                Login = "user1",
                OS = "Windows",
                StateProv = "63",
                UserAgent = "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko",
                VideoCard = "Gfx860m",
                Token = "ab8d78fb3a249b5c4502d14fab339c06f2e94376"
            });
            authInfoList.Add(new AuthInfo()
            {
                City = "Samara",
                Country = "Russia",
                DesktopResolution = "1920*1024",
                Ip = "94.100.120.4",
                Login = "user1",
                OS = "Windows",
                StateProv = "63",
                UserAgent = "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko",
                VideoCard = "Gfx860m",
                Token = "ab8d78fb3a249b5c4502d14fab339c06f2e94376"
            });
            authInfoList.Add(new AuthInfo()
            {
                City = "Samara",
                Country = "Russia",
                DesktopResolution = "1366*768",
                Ip = "94.100.120.5",
                Login = "user1",
                OS = "Windows",
                StateProv = "63",
                UserAgent = "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko",
                VideoCard = "Gfx860m",
                Token = "ab8d78fb3a249b5c4502d14fab339c06f2e94376"
            });
            authInfoList.Add(new AuthInfo()
            {
                City = "Samara",
                Country = "Russia",
                DesktopResolution = "1366*768",
                Ip = "94.100.120.4",
                Login = "user1",
                OS = "Windows",
                StateProv = "63",
                UserAgent = "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko",
                VideoCard = "Gfx860m",
                Token = "ab8d78fb3a249b5c4502d14fab339c06f2e94376"
            });
            authInfoList.Add(new AuthInfo()
            {
                City = "Tokio",
                Country = "Japan",
                DesktopResolution = "1920*1024",
                Ip = "88.88.88.88",
                Login = "user1",
                OS = "Windows",
                StateProv = "japan1",
                UserAgent = "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko",
                VideoCard = "Gfx860m",
                Token = "ab8d78fb3a249b5c4502d14fab339c06f2e94376"
            });
            AuthValidation authValidation = new AuthValidation((IAuthValidationSource)new LocalValidationSource());
            for (int index = 0; index < authInfoList.Count; ++index)
            {
                AuthInfo info = authInfoList[index];
                bool flag = authValidation.IsValidated(info, coefficient);
                Console.WriteLine(string.Format("{0}. City={1}, Country={2}, DesktopResolution={3}, Ip={4}, Login={5}, OS={6}, StateProv={7}, UserAgent={8}, VideoCard={9}, Token={10}", (object)index, (object)info.City, (object)info.Country, (object)info.DesktopResolution, (object)info.Ip, (object)info.Login, (object)info.OS, (object)info.StateProv, (object)info.UserAgent, (object)info.VideoCard, (object)info.Token));
                Console.WriteLine(string.Format("Result={0}", (object)flag));
                Console.WriteLine("");
            }
            Console.ReadKey();
        }
    }
}
