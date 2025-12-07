blackpearl.html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Black Pearl GmbH - Gastro Freelancer</title>
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="data:application/manifest+json;base64,eyJuYW1lIjoiQmxhY2sgUGVybCBHmbhIgLCJzaG9ydF9uYW1lIjoiQmxhY2tQZXJsIiwic3RhcnRfdXJsIjoiLyIsImRpc3BsYXkiOiJzdGFuZGFsb25lIiwiYmFja2dyb3VuZF9jb2xvciI6IiMwMDAwMDAiLCJ0aGVtZV9jb2xvciI6IiNEREFGMzdZb2JqY1RVaU1qUXlNVEl3TXpFd01qUXdOamN3IiwiaWNvbnMiOlt7InNyYyI6ImRhdGE6aW1hZ2Uvc3ZnK3htbDtjYXJldD0iL2xvZ28iLCJzaXplcyI6IjE5MngxOTIsMzg0eDM4NCIsInR5cGUiOiJpbWFnZS9zdmcifV19">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'pearl-black': '#000000',
                        'pearl-gold': '#D4AF37',
                        'pearl-bg': '#F8F9FA'
                    }
                }
            }
        }
    </script>
    
    <!-- FullCalendar -->
    <link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.15/index.global.min.css' rel='stylesheet' />
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.15/index.global.min.js'></script>
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        body { font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #F8F9FA 0%, #E9ECEF 100%); }
        .calendar-event-free { background-color: #FFD700 !important; border-color: #D4AF37 !important; }
        .calendar-event-taken { background-color: #28A745 !important; border-color: #20C997 !important; }
        .btn-touch { min-height: 48px; min-width: 48px; }
        .glass { backdrop-filter: blur(20px); background: rgba(255,255,255,0.9); border: 1px solid rgba(255,255,255,0.2); }
    </style>
</head>
<body class="min-h-screen p-4">
    <!-- Header -->
    <header class="glass rounded-2xl p-6 mb-8 shadow-2xl">
        <div class="flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-12 h-12 bg-gradient-to-br from-pearl-black to-pearl-gold rounded-2xl flex items-center justify-center">
                    <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"/>
                    </svg>
                </div>
                <div>
                    <h1 class="text-2xl font-bold bg-gradient-to-r from-pearl-black to-pearl-gold bg-clip-text text-transparent">Black Pearl GmbH</h1>
                    <p class="text-sm text-gray-600">Gastro & Events Freelancer</p>
                </div>
            </div>
            <div class="flex items-center space-x-2">
                <span id="userRole" class="px-3 py-1 bg-pearl-gold text-pearl-black text-xs font-bold rounded-full">Gast</span>
                <button id="loginBtn" class="btn-touch p-2 rounded-xl bg-pearl-gold hover:bg-pearl-black text-pearl-black hover:text-white transition-all">
                    <i data-lucide="user" class="w-5 h-5"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="space-y-6">
        <!-- Login Modal -->
        <div id="loginModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm hidden z-50 flex items-center justify-center p-4">
            <div class="glass rounded-3xl p-8 max-w-md w-full max-h-[90vh] overflow-y-auto">
                <div class="text-right mb-6">
                    <button id="closeLogin" class="text-2xl">&times;</button>
                </div>
                <h2 class="text-2xl font-bold text-pearl-black mb-6 text-center">Willkommen bei Black Pearl</h2>
                <div class="space-y-4">
                    <button class="w-full btn-touch bg-gradient-to-r from-pearl-black to-gray-8