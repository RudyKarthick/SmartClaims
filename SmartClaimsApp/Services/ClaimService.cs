using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;
using SmartClaimsApp.Models;

namespace SmartClaimsApp.Services
{
    public class ClaimService
    {
        private readonly HttpClient _http;

        public ClaimService(HttpClient http)
        {
            _http = http;
        }

        public async Task<ClaimResult?> AnalyzeClaimAsync(string summary)
        {
            var requestData = new { summary };
            try
            {
                var response = await _http.PostAsJsonAsync("http://127.0.0.1:5000/analyze", requestData);
                if (response.IsSuccessStatusCode)
                {
                    return await response.Content.ReadFromJsonAsync<ClaimResult>();
                }
            }
            catch
            {
                // Optional: Add logging
            }
            return null;
        }
    }
}
