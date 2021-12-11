using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public class LocalValidationSource : IAuthValidationSource
    {
        private ConcurrentDictionary<string, List<AuthInfo>> _validationTable;

        public LocalValidationSource() => this._validationTable = new ConcurrentDictionary<string, List<AuthInfo>>();

        public bool Check(AuthInfo authInfo, int coefficient)
        {
            if (!this._validationTable.ContainsKey(authInfo.Login))
                this._validationTable[authInfo.Login] = new List<AuthInfo>();
            bool flag = ValidationClass.Check(this._validationTable.ContainsKey(authInfo.Login) ? this._validationTable[authInfo.Login] : (List<AuthInfo>)null, authInfo, coefficient);
            if (flag)
                this._validationTable[authInfo.Login].Add(authInfo);
            return flag;
        }
    }
}
