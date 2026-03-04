import psutil
import time

print("========================================")
print("🚀 [CS2 专属加速] 正在清理后台闲杂进程...")
print("========================================")

# 专属黑名单 (已将 Wallpaper 设为免死金牌)
TARGETS = [
    "WidgetsPlatformRuntime.exe", # Windows 小组件 (极度吃内存)
    "wpscloudsvr.exe",            # WPS 偷偷同步的后台
    "wps.exe",
    "wpscenter.exe",
    "NeatDownloadManager.exe",    # 暂时不用的下载器
    "SearchApp.exe"               # Windows 搜索闲置进程
]

killed_count = 0

for proc in psutil.process_iter(['pid', 'name']):
    try:
        process_name = proc.info['name']
        if process_name in TARGETS:
            print(f"🎯 发现目标: {process_name} -> 🔫 击杀!")
            proc.kill()
            killed_count += 1
            time.sleep(0.2) # 停顿一下，制造黑客视觉效果
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("========================================")
if killed_count > 0:
    print(f"✅ 清理完毕！共干掉 {killed_count} 个拖后腿的进程。")
else:
    print("✅ 后台很干净，没有发现黑名单目标。")
print("🎮 魔霸 7 Plus 性能已满血，去炸鱼吧！")
print("========================================")

# 等待 3 秒后自动关闭窗口，深藏功与名
print("\n窗口将在 3 秒后自动销毁...")
time.sleep(3)