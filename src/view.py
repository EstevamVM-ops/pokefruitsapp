import flet as ft
import flet_camera as fc
import numpy as np

PIC_IVAL = 1

@ft.control
class CameraWidget(ft.Container):
    def init(self):
        self.preview = ft.Camera(
            expannd = True,
            preview_enabled=True 
        )
        self.content = self.preview
        self.camera_initialized = False
    def read_qrcode(self, on_detected_qrcode) -> 'str|None':
        pass
    async def init_camera(self):
        cameras = await self.preview.get_available_cameras()
        selected_camera = cameras[0]
        for cm in cameras:
            if cm.lens_direction == fc.CameraLensDirection.BACK:
                selected_camera = cm
        await self.preview.initialize(
            description=selected_camera
            resolution_preset=fc.ResolutionPreset.MEDIUM,
            enable_audio=False,
            image_format_grou=fc.ImageFormatGroup.JPEG
        )
        pass
    async def capture_qrcode(self):
        while True:
            if(self.camera_initialized):
                jpeg_bytes = await self.preview.take_picture()
    async def run(self):
        self.page.run_task(self.capture_qrcode)
        await self.init_camera()

@ft.control
class MainScreen(ft.Container):
    def init(self):
        self.camera = CameraWidget()
        self.read_btn = ft.Button('Ler', on_click=self.)
        self.qr_content = ft.Text(value = 'Nenhum')
        self.qr_content =  ft. Column(
            controls=[
                self.camera,
                self.read_btn,
                self.qr_content
            ]
        )
        async def on_click_read_btn(self, e):
            await self.camera.run()
            def om_detect_qrcode(self, data:str):