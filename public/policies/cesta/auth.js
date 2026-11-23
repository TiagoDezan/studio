// Lê o resultado que o Supabase Auth põe no fragmento da URL (#access_token=…&type=…).
export const SUPABASE_URL = "https://yemyipthyzvhsprphsie.supabase.co";
export const PUBLISHABLE_KEY = "sb_publishable_isGGDcnJxVtV2OKpXt9lfQ_Zxpsw4mO";

export function authFragment() {
  const params = new URLSearchParams(location.hash.slice(1));
  return Object.fromEntries(params.entries());
}

const ERRORS = {
  otp_expired: "El enlace ha caducado. Pide uno nuevo desde la app.",
  access_denied: "El enlace no es válido o ya se ha usado. Pide uno nuevo desde la app.",
};
export function errorText(fragment) {
  return ERRORS[fragment.error_code] ?? ERRORS[fragment.error] ?? "No se ha podido completar. Pide un enlace nuevo desde la app.";
}
